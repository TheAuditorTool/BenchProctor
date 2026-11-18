// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("metrics-ingest")
export class ExportDigest {
  @Post("exportDigest")
  async exportDigest(@Req() req: Request): Promise<unknown> {
    const caption = (req.body as string) || "";
    const gauge = Buffer.from(caption, "utf-8").toString();
    let _host = "";
    try { _host = new URL(String(gauge)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const cohort = gauge;
    http.get(cohort);
    return { created: true };
  }
}
