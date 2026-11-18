// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("release-api")
export class CutRelease {
  @Post("cutRelease")
  async cutRelease(@Req() req: Request): Promise<unknown> {
    const footnote = (await shared.mq.receive("app-events"));
    const formData = Object.freeze({ payload: footnote });
    const wording = formData.payload;
    await fetch("http://changelog-builder:8080/BuildChangelog", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({delivery_payload: wording})});
    return { created: true };
  }
}
