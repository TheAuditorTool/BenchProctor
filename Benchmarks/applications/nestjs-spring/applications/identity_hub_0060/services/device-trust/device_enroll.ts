// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("device-trust")
export class EnrollDevice {
  @Post("enrollDevice")
  async enrollDevice(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.body?.payload as string) || "";
    let persona;
    try { persona = JSON.parse(paragraph).value || paragraph; }
    catch (e) { persona = paragraph; }
    await fetch("http://profile-api:8080/UpdateProfile", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({identity_payload: persona})});
    return { created: true };
  }
}
