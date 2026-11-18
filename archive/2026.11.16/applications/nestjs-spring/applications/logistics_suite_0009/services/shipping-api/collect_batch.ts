// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("shipping-api")
export class CollectBatch {
  @Post("collectBatch")
  async collectBatch(@Req() req: Request): Promise<unknown> {
    const subject = (req.headers.host as string) || "";
    const parcel = `${subject}`;
    let _host = "";
    try { _host = new URL(String(parcel)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const consignment = parcel;
    http.get(consignment);
    return { created: true };
  }
}
