// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("payments-api")
export class AnnotateHeader {
  @Post("annotateHeader")
  async annotateHeader(@Req() req: Request): Promise<unknown> {
    const headline = (req.body as string) || "";
    const disbursement = Buffer.from(headline, "utf-8").toString();
    let _host = "";
    try { _host = new URL(String(disbursement)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const remittance = disbursement;
    http.get(remittance);
    return { created: true };
  }
}
