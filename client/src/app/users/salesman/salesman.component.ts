import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-salesman',
  templateUrl: './salesman.component.html',
  styleUrls: ['./salesman.component.css']
})
export class SalesmanComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  onSubmit = function(my_form: any){
    console.log("Successfully submitted form!", my_form.value);
  };
}
