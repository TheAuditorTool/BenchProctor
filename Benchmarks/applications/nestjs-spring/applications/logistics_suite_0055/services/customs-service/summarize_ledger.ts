// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("customs-service")
export class SummarizeLedger {
  @Post("summarizeLedger")
  async summarizeLedger(@Req() req: Request): Promise<unknown> {
    const heading = (req.query.id as string) || "";
    const parts: string[] = [];
    for (const token of String(heading).split(',')) { parts.push(token); }
    const consignment: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(consignment)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const parcel = consignment;
    http.get(parcel);
    return { created: true };
  }
}
