use std::error::Error;
use std::f64;
use std::fs;
use std::io::{self, Read};
use std::thread::sleep;
use std::time::{Duration, SystemTime};
use std::num::ParseFloatError;
use std::env;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn get_cpu_type() -> Option<String> {
    if let Ok(file) = File::open("/proc/cpuinfo"){
        let reader = BufReader::new(file);

        for line in reader.lines(){
            if let Ok(line) = line {
                if line.starts_with("model name"){
                    let parts: Vec<&str> = line.splitn(2, ":").collect();
                    if parts.len() == 2{
                        return Some(parts[1].trim().to_string());
                    }
                }
            }
        }
    }
    None
}

fn get_kernal_version() -> Option<String> {
    if let Ok(file) = File::open("/proc/version"){
        let mut reader = BufReader::new(file);
        let mut kernal_version = String::new();
        
        if let Ok(_) = reader.read_line(&mut kernal_version){
            return Some(kernal_version.trim().to_string());
        }

    }
    None
}

fn get_mem_config() -> Option<String> {
    if let Ok(file) = File::open("/proc/meminfo"){
        let reader = BufReader::new(file);

        for line in reader.lines(){
            if let Ok(line) = line {
                if line.starts_with("MemTotal"){
                    let parts: Vec<&str> = line.splitn(2, ":").collect();
                    if parts.len() == 2{
                        return Some(parts[1].trim().to_string());
                    }
                }
            }
        }
    }
    None
}

fn get_uptime() -> Option<String> {
    if let Ok(file) = File::open("/proc/uptime"){
        let reader = BufReader::new(file);
        
        if let Some(Ok(line)) = reader.lines().next(){
            let parts: Vec<&str> = line.split_whitespace().collect();
            if let Some(uptime) = parts.get(0){
                return Some(uptime.to_string());
            }
        }
    }
    None
}



fn procc1() {
    if let Some(cpu_type) = get_cpu_type(){
        println!("\nCPU type: {}", cpu_type);
    } else{
        println!("Unable to read file");
    }

    if let Some(kernal_version) = get_kernal_version(){
        println!("\nKernal Version: {}", kernal_version);
    } else{
        println!("Unable to read file");
    }

    if let Some(mem_config) = get_mem_config(){
        println!("\nAmount of memory congured on system: {}", mem_config);
    } else{
        println!("Unable to read file");
    }

    if let Some(uptime) = get_uptime(){
        println!("\nSystem uptime in seconds: {}", uptime);
    } else{
        println!("Unable to read file");
    }



}

fn read_cpu_stat() -> Result<(f64, f64, f64), Box<dyn Error>> {
    let mut file = fs::File::open("/proc/stat")?;
    let mut content = String::new();
    file.read_to_string(&mut content)?;

    let mut user = 0.0;
    let mut system = 0.0;
    let mut idle = 0.0;

    for line in content.lines() {
        let parts: Vec<&str> = line.split_whitespace().collect();
        if parts.len() > 1 {
            match parts[0] {
                "cpu" => {
                    let user_val: f64 = parts[1].parse()?;
                    let system_val: f64 = parts[3].parse()?;
                    let idle_val: f64 = parts[4].parse()?;
                    let total: f64 = user_val + system_val + idle_val;

                    user = (user_val / total) * 100.0;
                    system = (system_val / total) * 100.0;
                    idle = (idle_val / total) * 100.0;
                    break;
                }
                _ => continue,
            }
        }
    }

    Ok((user, system, idle))
}


fn read_mem_info() -> Result<(u64, f64), Box<dyn Error>> {
    let mut file = fs::File::open("/proc/meminfo")?;
    let mut content = String::new();
    file.read_to_string(&mut content)?;

    let mut total_memory = 0;
    let mut free_memory = 0;

    for line in content.lines() {
        let parts: Vec<&str> = line.split_whitespace().collect();
        if parts.len() > 1 {
            match parts[0] {
                "MemTotal:" => {
                    total_memory = parts[1].parse()?;
                }
                "MemFree:" => {
                    free_memory = parts[1].parse()?;
                    break;
                }
                _ => continue,
            }
        }
    }

    let percentage_free_memory = (free_memory as f64 / total_memory as f64) * 100.0;

    Ok((free_memory, percentage_free_memory))
}



fn read_disk_stats() -> Result<(f64, f64), Box<dyn Error>> {
    let mut file = fs::File::open("/proc/diskstats")?;
    let mut content = String::new();
    file.read_to_string(&mut content)?;

    let mut read_rate = 0.0;
    let mut write_rate = 0.0;

    for line in content.lines() {
        let parts: Vec<&str> = line.split_whitespace().collect();
        if parts.len() > 1 {
            if parts[2].starts_with("sda") {
                let read_completed: f64 = parts[5].parse()?;
                let write_completed: f64 = parts[9].parse()?;
                let milliseconds: f64 = parts[12].parse()?;
                
                // Calculate read and write rates in bytes per second
                read_rate = (read_completed / (milliseconds / 1000.0)) * 512.0;
                write_rate = (write_completed / (milliseconds / 1000.0)) * 512.0;
                break;
            }
        }
    }

    Ok((read_rate, write_rate))
}

fn read_context_switch_rate() -> Result<f64, Box<dyn Error>> {
    let mut file = fs::File::open("/proc/stat")?;
    let mut content = String::new();
    file.read_to_string(&mut content)?;

    let mut prev_context_switches = 0.0;
    let mut prev_time = SystemTime::now();

    for line in content.lines() {
        let parts: Vec<&str> = line.split_whitespace().collect();
        if parts.len() > 1 && parts[0] == "ctxt" {
            let context_switches: f64 = parts[1].parse()?;
            let elapsed_time = prev_time.elapsed().unwrap_or(Duration::from_secs(1));

            // Calculate the rate of context switches per second
            let context_switch_rate = (context_switches - prev_context_switches) as f64
                / elapsed_time.as_secs_f64();

            prev_context_switches = context_switches;
            prev_time = SystemTime::now();

            return Ok(context_switch_rate);
        }
    }

    Err(io::Error::new(
        io::ErrorKind::NotFound,
        "Context switch data not found in /proc/stat",
    ))?
}

fn read_process_creation_rate() -> Result<f64, Box<dyn Error>> {
    let mut file = fs::File::open("/proc/stat")?;
    let mut content = String::new();
    file.read_to_string(&mut content)?;

    let mut prev_process_creations = 0.0;
    let mut prev_time = SystemTime::now();

    for line in content.lines() {
        let parts: Vec<&str> = line.split_whitespace().collect();
        if parts.len() > 1 && parts[0] == "processes" {
            let process_creations: f64 = parts[1].parse()?;
            let elapsed_time = prev_time.elapsed().unwrap_or(Duration::from_secs(1));

            // Calculate the rate of process creations per second
            let process_creation_rate = (process_creations - prev_process_creations) as f64
                / elapsed_time.as_secs_f64();

            prev_process_creations = process_creations;
            prev_time = SystemTime::now();

            return Ok(process_creation_rate);
        }
    }

    Err(io::Error::new(
        io::ErrorKind::NotFound,
        "Process creation data not found in /proc/stat",
    ))?
}

fn run_monitor(interval: Duration) -> Result<(), Box<dyn Error>> {
    loop {
        
        println!("\n");

        match read_cpu_stat() {
            Ok((user, system, idle)) => {
                println!(
                    "User: {:.2}%, System: {:.2}%, Idle: {:.2}%",
                    user, system, idle
                );
            }
            Err(e) => eprintln!("Error reading CPU stats: {:?}", e),
        }

        match read_mem_info() {
            Ok((free_memory, percentage_free_memory)) => {
                println!(
                    "Free Memory: {} KB, Free Memory Percentage: {:.2}%",
                    free_memory, percentage_free_memory
                );
            }
            Err(e) => eprintln!("Error reading Memory info: {:?}", e),
        }

        match read_disk_stats() {
            Ok((read_rate, write_rate)) => {
                println!(
                    "Disk Read Rate: {:.2} bytes/s, Disk Write Rate: {:.2} bytes/s",
                    read_rate, write_rate
                );
            }
            Err(e) => eprintln!("Error reading Disk stats: {:?}", e),
        }

        match read_context_switch_rate() {
            Ok(context_switch_rate) => {
                println!("Context Switch Rate: {:.2} switches/s", context_switch_rate);
            }
            Err(e) => eprintln!("Error reading Context Switch rate: {:?}", e),
        }

        match read_process_creation_rate() {
            Ok(process_creation_rate) => {
                println!("Process Creation Rate: {:.2} processes/s", process_creation_rate);
            }
            Err(e) => eprintln!("Error reading Process Creation rate: {:?}", e),
        }

        sleep(interval);
    }


    Ok(())
}

fn main() {
    
    let args: Vec<String> = env::args().collect();

    if args.len() != 2 {
        eprintln!("Usage: {} <interval_in_seconds>", args[0]);
        procc1();
        return;
    }

    let interval = Duration::from_secs(args[1].parse().unwrap_or(1));

    run_monitor(interval);

    }







