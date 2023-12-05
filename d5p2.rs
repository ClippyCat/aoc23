use std::fs::File;
use std::io::{BufReader, BufRead, Write};

fn remove(file_name: &str, new_file: &str) {
    let mut lines = Vec::new();
    if let Ok(file) = File::open(file_name) {
        let reader = BufReader::new(file);
        for line in reader.lines() {
            if let Ok(line_content) = line {
                if let Some(idx) = line_content.find(':') {
                    let mut modified_line = line_content[idx + 1..].trim().to_string();
                    modified_line.push('\n');
                    lines.push(modified_line);
                }
            }
        }
    }

    if let Ok(mut file) = File::create(new_file) {
        for line in lines {
            file.write_all(line.as_bytes()).unwrap();
        }
    }
}

fn seeds(new_file: &str) -> Vec<i32> {
    if let Ok(file) = File::open(new_file) {
        let mut lines = Vec::new();
        let reader = BufReader::new(file);
        for line in reader.lines() {
            if let Ok(content) = line {
                lines.push(content);
            }
        }
        if let Some(first_line) = lines.first() {
            return first_line.split_whitespace().map(|s| s.parse().unwrap()).collect();
        }
    }
    Vec::new()
}

fn split_maps(new_file: &str) -> Vec<String> {
    if let Ok(file) = File::open(new_file) {
        let mut lines = Vec::new();
        let reader = BufReader::new(file);
        for line in reader.lines().skip(1) {
            if let Ok(content) = line {
                lines.push(content);
            }
        }
        return lines.join("\n\n").split("\n\n").map(String::from).collect();
    }
    Vec::new()
}

fn line_to_nums(line: &str) -> (i32, i32, i32) {
    let nums: Vec<i32> = line.split_whitespace().map(|s| s.parse().unwrap()).collect();
    (nums[0], nums[1], nums[2])
}

fn sec_to_num(section: &str) -> Vec<(i32, i32, i32)> {
    section.lines().map(|line| line_to_nums(line)).collect()
}

fn calc(data: &[Vec<(i32, i32, i32)>], v: i32) -> i32 {
    let mut v = v;
    for deez in data {
        for l in deez {
            let dest = l.0;
            let src = l.1;
            let leng = l.2;
            if src <= v && v < src + leng {
                v = dest + v - src;
                break;
            }
        }
    }
    v
}

fn main() {
    let file_name = "p.txt";
    let new_file = "new.txt";

    remove(file_name, new_file);

    let seeds_list = seeds(new_file);
    // println!("{:?}", seeds_list);

    let maps = split_maps(new_file);
    // println!("{:?}", maps);

    let data: Vec<Vec<(i32, i32, i32)>> = maps.iter().map(|sec| sec_to_num(sec)).collect();
    // println!("{:?}", data);

    let mut result = Vec::new();

    for i in (0..seeds_list.len()).step_by(2) {
        let start_seed = seeds_list[i];
        let length = seeds_list[i + 1];
        for s in start_seed..start_seed + length {
            result.push(calc(&data, s));
        }
    }
    if let Some(min_result) = result.iter().min() {
        println!("{}", min_result);
    }
}
