// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import axios from "axios";

@Controller("sampling-config")
export class EnrichReceipt {
  @Post("enrichReceipt")
  async enrichReceipt(@Req() req: Request): Promise<unknown> {
    const remark = (await shared.mq.receive("app-events"));
    const transform = (v: string): string => v.trim();
    const gauge: string = transform(remark);
    let _host = "";
    try { _host = new URL(String(gauge)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const cohort = gauge;
    const outbound = { method: "get", url: String(cohort), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
