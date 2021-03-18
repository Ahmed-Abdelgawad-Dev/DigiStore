var updateBtns = document.getElementsByClassName("update-cart");
for (let i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener("click", function () {
		let productId = this.dataset.product;
		let action = this.dataset.action;
		console.log("productID", productId, "action", action);
		console.log("useris:", user);
		if (user === "AnonymousUser") {
			// addCookieItem();
			console.log("test");
		} else {
			updateUserOrder(productId, action);
		}
	});
}

// function addCookieItem(productId, action) {
// 	console.log("not logged in");

// 	if(action == 'add') {
// 		if(cart[prodoductId] == undefined) {
// 			cart[productId] = {
// 				'quantity': 1
// 			};
// 		} else {
// 			cart[productId]['quantity'] += 1;
// 		}
// 	}
// 	if(action == 'remove') {
// 		cart[productId]["quantity"]  -= 1;
// 		if(cart[productId]["quantity"] <= 0) {
// 			console.log("remove item");
// 			delete cart[productId];
// 		}
// 	}
// 	console.log('cart: ', cart);
// 	document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/";
// }

function updateUserOrder(productId, action) {
	console.log("user is logged in sending data ...");
	var url = "/update_item/";
	fetch(url, {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"X-CSRFToken": csrftoken,
			},
			body: JSON.stringify({
				productId: productId,
				action: action,
			}),
		})
		.then((response) => {
			return response.json();
		})
		.then((data) => {
			console.log("data: ", data);
			location.reload();
		});
}



function addCookieItem(productId, action) {
  console.log("User is not authenticated");

  if (action == "add") {
    if (cart[productId] == undefined) {
      cart[productId] = { quantity: 1 };
    } else {
      cart[productId]["quantity"] += 1;
    }
  }

  if (action == "remove") {
    cart[productId]["quantity"] -= 1;

    if (cart[productId]["quantity"] <= 0) {
      console.log("Item should be deleted");
      delete cart[productId];
    }
  }
  console.log("CART:", cart);
  document.cookie = "cart=" + JSON.stringify(cart) + ";domain=;path=/";

  location.reload();
}