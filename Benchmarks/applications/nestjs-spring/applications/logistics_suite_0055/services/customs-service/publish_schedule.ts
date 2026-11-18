// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("customs-service")
export class PublishSchedule {
  @Post("publishSchedule")
  async publishSchedule(@Req() req: Request): Promise<unknown> {
    const heading = (req.body.payload as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(heading);
    const consignment: string = readInput();
    let _host = "";
    try { _host = new URL(String(consignment)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const parcel = consignment;
    http.get(parcel);
    return { created: true };
  }
}
