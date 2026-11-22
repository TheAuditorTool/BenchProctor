// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("manifest-builder")
export class CompactReceipt {
  @Post("compactReceipt")
  async compactReceipt(@Req() req: Request): Promise<unknown> {
    const transcript = (req.headers["x-custom-header"] as string) || "";
    const parts: string[] = [];
    for (const token of String(transcript).split(',')) { parts.push(token); }
    const consignment: string = parts.join(',');
    if (!/^(asc|desc|name|created)$/.test(String(consignment))) { throw new BadRequestException({error:"invalid"}); }
    const parcel = consignment;
    childProcess.execSync("echo " + parcel);
    return { created: true };
  }
}
