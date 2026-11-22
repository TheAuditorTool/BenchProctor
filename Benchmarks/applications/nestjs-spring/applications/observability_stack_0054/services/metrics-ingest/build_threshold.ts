// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import axios from "axios";

@Controller("metrics-ingest")
export class BuildThreshold {
  @Post("buildThreshold")
  async buildThreshold(@Req() req: Request): Promise<unknown> {
    const excerpt = (await shared.mq.receive("app-events"));
    const transform = (v: string): string => v.trim();
    const cohort: string = transform(excerpt);
    let _host = "";
    try { _host = new URL(String(cohort)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const gauge = cohort;
    const outbound = { method: "get", url: String(gauge), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
