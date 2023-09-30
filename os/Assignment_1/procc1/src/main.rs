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


fn main(){
    procc1();
}
