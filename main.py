from factories import word90_factory, word00_factory, word10_factory, word25_factory

#open config file
f = open('configuration.txt', 'r')

for line in f:

    line = line.strip() #trying to debug removing any extra whitespace

    match line:
        case "Word90":

            factory = word90_factory()
        case "Word00":

            factory = word00_factory()
        case "Word10":

            factory = word10_factory()
        case "Word25":

            factory = word25_factory()
        case _:

            print("ERROR- UNKNOWN CONFIG FOUND IN FILE.\n")
            continue

    if factory: #if factory is instantiated (following modified singleton pattern)
        button = factory.createButton()
        panel = factory.createPanel()
        textbox = factory.createTextbox()

        # Test components
        button.testComponent()
        panel.testComponent()
        textbox.testComponent()
    
