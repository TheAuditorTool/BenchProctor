// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("reservation-service")
export class BuildSchedule {
  @Post("buildSchedule")
  async buildSchedule(@Req() req: Request): Promise<unknown> {
    const transcript = (req.headers.host as string) || "";
    const backorder = `${transcript}`;
    let _host = "";
    try { _host = new URL(String(backorder)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const restock = backorder;
    http.get(restock);
    return { created: true };
  }
}
