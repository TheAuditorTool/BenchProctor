// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("tracking-service")
export class ExportBundle {
  @Post("exportBundle")
  async exportBundle(@Req() req: Request): Promise<unknown> {
    const caption = (req.body as string) || "";
    const _raw = caption;
    const consignment = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!["ls", "cat", "date", "whoami"].includes(consignment)) { throw new ForbiddenException({error:'forbidden'}); }
    const parcel = consignment;
    childProcess.execSync("echo " + parcel);
    return { created: true };
  }
}
