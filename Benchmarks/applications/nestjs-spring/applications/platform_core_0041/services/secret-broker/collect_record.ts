// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("secret-broker")
export class CollectRecord {
  @Post("collectRecord")
  async collectRecord(@Req() req: Request): Promise<unknown> {
    const passage = (req.headers["x-forwarded-for"] as string) || "";
    let persona;
    try { persona = JSON.parse(passage).value || passage; }
    catch (e) { persona = passage; }
    fs.unlinkSync("/var/app/data/" + persona);
    return { created: true };
  }
}
