// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("macro-service")
export class AnnotateReport {
  @Post("annotateReport")
  async annotateReport(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.host as string) || "";
    const grievance = `${summary}`;
    let _host = "";
    try { _host = new URL(String(grievance)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const inquiry = grievance;
    http.get(inquiry);
    return { created: true };
  }
}
