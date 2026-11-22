// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("profile-api")
export class MergeReceipt {
  @Post("mergeReceipt")
  async mergeReceipt(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.body as string) || "";
    const persona = Buffer.from(paragraph, "utf-8").toString();
    let _host = "";
    try { _host = new URL(String(persona)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const blurb = persona;
    http.get(blurb);
    return { created: true };
  }
}
