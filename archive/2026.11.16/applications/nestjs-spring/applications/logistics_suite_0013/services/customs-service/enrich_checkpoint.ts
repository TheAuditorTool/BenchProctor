// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("customs-service")
export class EnrichCheckpoint {
  @Post("enrichCheckpoint")
  async enrichCheckpoint(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers.host as string) || "";
    const parcel = `${footnote}`;
    let _host = "";
    try { _host = new URL(String(parcel)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const consignment = parcel;
    http.get(consignment);
    return { created: true };
  }
}
