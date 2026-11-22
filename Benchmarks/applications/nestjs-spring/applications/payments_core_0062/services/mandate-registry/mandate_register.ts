// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("mandate-registry")
export class RegisterMandate {
  @Post("registerMandate")
  async registerMandate(@Req() req: Request): Promise<unknown> {
    const headline = (req.headers.host as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const disbursement: string = normalize(headline);
    await fetch("http://payments-api:8080/AuthorizePayment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({payments_payload: disbursement})});
    return { created: true };
  }
}
