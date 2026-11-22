// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";
import * as zod from "zod";

@Controller("customs-service")
export class AuditConfig {
  @Post("auditConfig")
  async auditConfig(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers["user-agent"] as string) || "";
    const consignment = summary != null ? summary : '';
    const _parsed = zod.z.string().regex(/^[a-zA-Z0-9 _.%\-]+$/).safeParse(String(consignment));
    if (!_parsed.success) { throw new BadRequestException({error:"invalid"}); }
    const parcel = _parsed.data;
    childProcess.exec("echo " + parcel, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
