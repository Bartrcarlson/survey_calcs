
fn dd_to_dms(dd: f64) -> [i16;3] {

    let mut dms:[i16;3] = [0,0,0];
    dms[0] = dd as i16;
    let m = (dd % 1.0) * 60.0;
    dms[1] = m as i16;
    let s = (m % 1.0) * 60.0;
    dms[2] = s.round() as i16; 

    if dms[1] >= 60{
        dms[0] = dms[0] + ((dms[1]/60) as i16);
        dms[1] = dms[1] - (((dms[1]/60) * 60) as i16);
    }

    if dms[2] >= 60{
        dms[1] = dms[1] + ((dms[1]/60) as i16);
        dms[2] = dms[2] - (((dms[1]/60) * 60) as i16);
    }

return dms
}

fn dms_to_dd(dms:[i16; 3]) -> f64 {
    return ((dms[0] as f64) + (dms[1] as f64 /60.0) + (dms[2] as f64 / 3600.0))
}

enum Direction {
    N,
    W,
    S,
    E,
}

struct Bearing {
    ns: Direction,
    bearing: [i16;3],
    ew: Direction
}

fn az_to_bearing(az: f64) -> Bearing {

    // let mut bearing: [i16;3] = [0;3];

    if az < 0.0 || az>360.0 {
        panic!("Invalid az")
    }
    if az >=270.0 || az<=90.0{
        let mut bearing = Bearing{ns: Direction::N, bearing:[0,0,0], ew: Direction::E};
    }
    else{
        let mut bearing = Bearing{ns: Direction::S, bearing:[0,0,0], ew: Direction::E};
    }

    if az >= 0.0 && az <= 180.0{
        bearing[2] = "E"
        let mut bearing = Bearing{ew: Direction::E};
    }
    else{
        bearing[2] = "w"}

    if az <= 90.0{
        bearing[1] = az}
    else if  az >= 270.0{
        bearing[1] = 360.0 - az}
    else if az > 90.0 && az < 180.0{
        bearing[1] = 180.0 - az}
    else if az >= 180.0 && az < 270.0{
        bearing[1] = az - 180.0}
}

fn main() {
    println!("{:?}", dd_to_dms(330.1234));
    println!("{:?}", dms_to_dd([16,0,60]));
}
