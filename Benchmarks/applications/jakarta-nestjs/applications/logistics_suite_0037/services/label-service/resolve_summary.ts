// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

@Controller("label-service")
export class ResolveSummary {
  @Post("resolveSummary")
  async resolveSummary(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body.payload as string) || "";
    const _raw = footnote;
    const consignment = (_raw && _raw.length > 0) ? _raw : 'default';
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(String(consignment));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const parcel = _parsed.data;
    childProcess.execSync("echo " + parcel);
    return { created: true };
  }
}
