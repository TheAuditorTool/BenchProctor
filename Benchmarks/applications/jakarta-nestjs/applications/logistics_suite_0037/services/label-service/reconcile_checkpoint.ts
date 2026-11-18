// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("label-service")
export class ReconcileCheckpoint {
  @Post("reconcileCheckpoint")
  async reconcileCheckpoint(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body?.variables?.input as string) || "";
    const payload = { get value() { return footnote; } };
    const consignment = payload.value;
    if (!/^(asc|desc|name|created)$/.test(String(consignment))) { throw new BadRequestException({error:"invalid"}); }
    const parcel = consignment;
    const fileContent = fs.readFileSync("/var/app/data/" + parcel, "utf8");
    return fileContent;
  }
}
