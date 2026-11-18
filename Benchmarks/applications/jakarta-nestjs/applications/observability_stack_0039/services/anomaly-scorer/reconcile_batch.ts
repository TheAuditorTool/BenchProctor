// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("anomaly-scorer")
export class ReconcileBatch {
  @Post("reconcileBatch")
  async reconcileBatch(@Req() req: Request): Promise<unknown> {
    const caption = (req.body as string) || "";
    const cohort = Buffer.from(caption, "utf-8").toString();
    let _host = "";
    try { _host = new URL(String(cohort)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const gauge = cohort;
    http.get(gauge);
    return { created: true };
  }
}
