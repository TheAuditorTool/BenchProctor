// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("carrier-gateway")
export class MergeRoster {
  @Post("mergeRoster")
  async mergeRoster(@Req() req: Request): Promise<unknown> {
    const citation = ((req as any).files?.[0]?.originalname as string) || "";
    const tokens = String(citation).split(',').filter((t) => t.length > 0);
    const parcel = tokens.join(' ');
    let _host = "";
    try { _host = new URL(String(parcel)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const consignment = parcel;
    http.get(consignment);
    return { created: true };
  }
}
