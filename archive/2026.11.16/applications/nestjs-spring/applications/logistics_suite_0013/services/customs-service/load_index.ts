// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("customs-service")
export class LoadIndex {
  @Post("loadIndex")
  async loadIndex(@Req() req: Request): Promise<unknown> {
    const footnote = (req.cookies?.session_token as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const parcel: string = normalize(footnote);
    if (!/^(asc|desc|name|created)$/.test(String(parcel))) { throw new BadRequestException({error:"invalid"}); }
    const consignment = parcel;
    childProcess.execSync("echo " + consignment);
    return { created: true };
  }
}
