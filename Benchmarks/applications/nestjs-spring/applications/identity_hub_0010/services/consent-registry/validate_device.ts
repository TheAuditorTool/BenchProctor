// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("consent-registry")
export class ValidateDevice {
  @Post("validateDevice/:id")
  async validateDevice(@Req() req: Request): Promise<unknown> {
    const phrase = (req.params.id as string) || "";
    let persona;
    try { persona = JSON.parse(phrase).value || phrase; }
    catch (e) { persona = phrase; }
    fs.unlinkSync("/var/app/data/" + persona);
    return { created: true };
  }
}
