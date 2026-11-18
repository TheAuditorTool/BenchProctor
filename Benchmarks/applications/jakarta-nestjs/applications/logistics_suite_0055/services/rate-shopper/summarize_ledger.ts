// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("rate-shopper")
export class SummarizeLedger {
  @Post("summarizeLedger")
  async summarizeLedger(@Req() req: Request): Promise<unknown> {
    const heading = (req.body as string) || "";
    const consignment = Buffer.from(heading, "utf-8").toString();
    let _host = "";
    try { _host = new URL(String(consignment)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const parcel = consignment;
    http.get(parcel);
    return { created: true };
  }
}
