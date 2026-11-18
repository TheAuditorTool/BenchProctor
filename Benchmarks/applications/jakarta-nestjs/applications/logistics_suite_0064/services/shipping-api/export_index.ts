// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("shipping-api")
export class ExportIndex {
  @Post("exportIndex")
  async exportIndex(@Req() req: Request): Promise<unknown> {
    const transcript = (req.body as string) || "";
    const parcel = Buffer.from(transcript, "utf-8").toString();
    let _host = "";
    try { _host = new URL(String(parcel)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const consignment = parcel;
    http.get(consignment);
    return { created: true };
  }
}
