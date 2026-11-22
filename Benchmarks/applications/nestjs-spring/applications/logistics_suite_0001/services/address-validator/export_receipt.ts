// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("address-validator")
export class ExportReceipt {
  @Post("exportReceipt")
  async exportReceipt(@Req() req: Request): Promise<unknown> {
    const quotation = (req.body as string) || "";
    const _raw = quotation;
    const parcel = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!["ls", "cat", "date", "whoami"].includes(parcel)) { throw new ForbiddenException({error:'forbidden'}); }
    const consignment = parcel;
    childProcess.execSync("echo " + consignment);
    return { created: true };
  }
}
