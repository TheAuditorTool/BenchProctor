// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("shipping-api")
export class CollectReport {
  @Post("collectReport")
  async collectReport(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers.referer as string) || "";
    const _raw = citation;
    const parcel = (_raw && _raw.length > 0) ? _raw : 'default';
    if (!/^(asc|desc|name|created)$/.test(String(parcel))) { throw new BadRequestException({error:"invalid"}); }
    const consignment = parcel;
    childProcess.exec("echo " + consignment, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
