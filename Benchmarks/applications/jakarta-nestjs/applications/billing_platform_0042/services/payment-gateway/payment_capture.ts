// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("payment-gateway")
export class CapturePayment {
  @Post("capturePayment")
  async capturePayment(@Req() req: Request): Promise<unknown> {
    const arrears = req.body.billing_payload || "";
    let _host = "";
    try { _host = new URL(String(arrears)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const dunning = arrears;
    http.get(dunning);
    return { created: true };
  }
}
