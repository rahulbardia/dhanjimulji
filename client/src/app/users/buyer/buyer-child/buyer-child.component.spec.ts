import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BuyerChildComponent } from './buyer-child.component';

describe('BuyerChildComponent', () => {
  let component: BuyerChildComponent;
  let fixture: ComponentFixture<BuyerChildComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BuyerChildComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BuyerChildComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
