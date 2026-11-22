// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import axios from "axios";

@Controller("carrier-gateway")
export class LoadPolicy {
  @Post("loadPolicy")
  async loadPolicy(@Req() req: Request): Promise<unknown> {
    const citation = (await shared.mq.receive("app-events"));
    const transform = (v: string): string => v.trim();
    const parcel: string = transform(citation);
    let _host = "";
    try { _host = new URL(String(parcel)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const consignment = parcel;
    const outbound = { method: "get", url: String(consignment), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
