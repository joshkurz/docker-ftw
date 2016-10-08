// main.go

package main

import (
	"log"
	"net/http"

	"github.com/caarlos0/env"
)

type config struct {
	Port string `env:"PORT" envDefault:"3000"`
}

func main() {
	cfg := config{}
	env.Parse(&cfg)
	log.Printf("Docker FTW listening on %v\n", cfg.Port)
	err := http.ListenAndServe(":"+cfg.Port, http.FileServer(http.Dir("static")))
	log.Fatal(err)
}
