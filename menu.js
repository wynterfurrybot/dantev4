function get(msg, item, id, callback) {


		if(item == "!beer" || item == "!whiskey" || item == "!vodka" || item == "!martini" || item === "rum"){

			if(id === "347912401812848640")
			{
				if (msg.channel.id === "463840305129455616"){
					callback("I shouldn't really serve this.. but here's a " + item.replace("!","") + "\nEnjoy!");
					return;
				}
				else{
				callback("Darkmane told me not to serve you anything alcoholic.. ");
				return;
				}
			}

	      callback("thanks for ordering a " + item.replace("!","") + "! \n\nDrink responsibly!")
			}

			else if(item == "!cola" || item == "!tea" || item == "!coffee" || item == "!coke" )
				{
					 callback("thanks for ordering a " + item.replace("!","") + "! \n\nWe respect your decision to not get wasted!")
				}


				else if (item === "!pineapple" || item === "!pineapples"){
					callback(":pineapple:");
				}

				else if (item === "!sandwich" || item === "!steak" || item === "pizza"){
					callback("thanks for ordering a " + item.replace("!","") + "!");
				}






	else{
		callback("Not a drink");
	}
}

module.exports = {
  get: get
}

