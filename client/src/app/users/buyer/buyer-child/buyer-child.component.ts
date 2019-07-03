import 'rxjs/Rx';
import { CommonService } from "./../../../shared/common.service"
import { Http } from '@angular/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from "@angular/router";

@Component({
  selector: 'app-buyer-child',
  templateUrl: './buyer-child.component.html',
  styleUrls: ['./buyer-child.component.css']
})
export class BuyerChildComponent implements OnInit {
  data: any = null;
  endpoint = '/users/buyerchild/';
  buyer = null;
  constructor(private http: Http, private _buyerService: CommonService, private route: ActivatedRoute) {
  }


  ngOnInit() {
    this.route.paramMap.subscribe(params => {
    this.buyer = params.get("id");
      console.log("Buyer_id passed is %s", this.buyer);
  })
  }

  onSubmit = function(my_form: any){
        my_form.buyer = this.buyer;
        console.log("buyer child form", my_form);
        this._buyerService.postForm(this.endpoint, my_form)
            .subscribe(
            data => {
              console.log("data posted", data);
            });
  };

  get_data = function(my_form: any){
        this._buyerService.getData(this.endpoint, {'buyer': this.buyer})
            .subscribe((response) => {
        console.log("API sent", response);
      });
  };
}
