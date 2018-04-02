import 'rxjs/Rx';
import { CommonService } from "./../../shared/common.service"
import { Http } from '@angular/http';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-supplier-inventory',
  templateUrl: './supplier-inventory.component.html',
  styleUrls: ['./supplier-inventory.component.css']
})
export class SupplierInventoryComponent implements OnInit {
  data: any = null;
  endpoint = '/users/supplierinventory/';
  constructor(private http: Http, private _service: CommonService) {
  }

  ngOnInit() {
  }

  onSubmit = function(my_form: any){
        this._service.postForm(this.endpoint, my_form)
            .subscribe(
            data => {
              console.log("data posted", data);
            });
  };

  get_data = function(){
    console.log("Get data called");
        this._service.getData(this.endpoint, 5)
            .subscribe((response) => {
        console.log("API sent", response);
      });
  };
}

