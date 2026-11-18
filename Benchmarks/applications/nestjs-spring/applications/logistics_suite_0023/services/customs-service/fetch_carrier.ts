// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

@Controller("customs-service")
export class FetchCarrier {
  @Post("fetchCarrier")
  async fetchCarrier(@Req() req: Request): Promise<unknown> {
    const caption = (req.cookies?.session_token as string) || "";
    const parts: string[] = [];
    for (const token of String(caption).split(',')) { parts.push(token); }
    const parcel: string = parts.join(',');
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(String(parcel));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const consignment = _parsed.data;
    childProcess.execSync("echo " + consignment);
    return { created: true };
  }
}
