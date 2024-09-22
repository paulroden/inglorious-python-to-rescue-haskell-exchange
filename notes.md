Steps:
 - search for speaker name or other key phrase
 - the speaker name should yield an element such as:
    ```html
    <p class="speakers">{{speaker_name}}</p>
    ```
    this `<p>` element is within the
        `<td "class="title">` element
        of a `<tr>`
        of a `<tbody>`
        of a `<table>`
        of a`<div class="multitrack-schedule__single__inner">`
        of a `<a class="multitrack-schedule__single" data-reveal-id="modal-sessiondetails-14192-4462-729">`,
        i.e.
    the value associated with the `data-reveal-id` attribute
      below the `<a class="multitrack-schedule__single" data-reveal-id="modal-sessiondetails-14192-4462-729">` element,
      there's a hidden `<div class="reveal-modal large" data-reveal="" id="modal-sessiondetails-14192-4462-729">`
      which has all the juicy details of the talk!

 - tracing up the DOM from this, there's an element like:
    ```html
    <a class="multitrack-schedule__single" data-reveal-id="modal-sessiondetails-14192-4462-729">...
      ```
    which is
