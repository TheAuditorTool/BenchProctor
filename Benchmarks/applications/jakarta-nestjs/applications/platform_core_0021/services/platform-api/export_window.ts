// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

@Controller("platform-api")
export class ExportWindow {
  @Post("exportWindow")
  async exportWindow(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.body.payload as string) || "";
    const _raw = excerpt;
    const handshake = (_raw && _raw.length > 0) ? _raw : 'default';
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(String(handshake));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const persona = _parsed.data;
    childProcess.execSync("echo " + persona);
    return { created: true };
  }
}
