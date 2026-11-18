// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("shipping-api")
export class ExportProfile {
  @Post("exportProfile")
  async exportProfile(@Req() req: Request): Promise<unknown> {
    const phrase = (req.body.payload as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(phrase);
    const parcel: string = readInput();
    let _host = "";
    try { _host = new URL(String(parcel)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const consignment = parcel;
    http.get(consignment);
    return { created: true };
  }
}
