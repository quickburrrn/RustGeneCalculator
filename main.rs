#[macro_use] extern crate rocket;

#[get("/")]
fn home() -> &'static str {
    "Welcome to the rust crossbreed api"
}

#[get("/hello")]
fn hello() -> &'static str {
    "Hello, world!"
}

#[launch]
fn rocket() -> _ {
    rocket::build().mount("/", routes![home, hello])
}