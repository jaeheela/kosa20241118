class Coffee {
    constructor(name) {
        this.name = name;
    }
}

class Latte extends Coffee {
    constructor() {
        super("Latte");
    }
}

class Espresso extends Coffee {
    constructor() {
        super("Espresso");
    }
}

class CoffeeFactory {
    static createCoffee(type) {
        const factory = factoryList[type];
        if (factory) {
            return factory.createCoffee();
        } else {
            throw new Error("Unknown coffee type");
        }
    }
}

class LatteFactory {
    static createCoffee() {
        return new Latte();
    }
}

class EspressoFactory {
    static createCoffee() {
        return new Espresso();
    }
}

const factoryList = {
    Latte: LatteFactory,
    Espresso: EspressoFactory
};

// 사용 예
const latte = CoffeeFactory.createCoffee("Latte");
console.log(latte.name); // Latte

const espresso = CoffeeFactory.createCoffee("Espresso");
console.log(espresso.name); // Espresso
