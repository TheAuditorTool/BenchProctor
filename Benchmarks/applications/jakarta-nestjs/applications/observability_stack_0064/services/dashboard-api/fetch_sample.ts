// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("dashboard-api")
export class FetchSample {
  @Post("fetchSample")
  async fetchSample(@Req() req: Request): Promise<unknown> {
    const tagline = (req.cookies?.session_token as string) || "";
    const gauge = tagline != null ? tagline : '';
    let _host = "";
    try { _host = new URL(String(gauge)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const cohort = gauge;
    http.get(cohort);
    return { created: true };
  }
}
