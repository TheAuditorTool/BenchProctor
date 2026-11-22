// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("dashboard-api")
export class EnrichReport {
  @Post("enrichReport/:id")
  async enrichReport(@Req() req: Request): Promise<unknown> {
    const tagline = (req.params.id as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const gauge: string = normalize(tagline);
    let _host = "";
    try { _host = new URL(String(gauge)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const cohort = gauge;
    http.get(cohort);
    return { created: true };
  }
}
