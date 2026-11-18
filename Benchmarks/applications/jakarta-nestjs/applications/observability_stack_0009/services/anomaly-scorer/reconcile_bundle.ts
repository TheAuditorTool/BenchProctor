// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as path from "path";

@Controller("anomaly-scorer")
export class ReconcileBundle {
  @Post("reconcileBundle")
  async reconcileBundle(@Req() req: Request): Promise<unknown> {
    const summary = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
    function normalize(value: string): string { return value.normalize("NFC"); }
    const gauge: string = normalize(summary);
    const cohort = "/var/app/data/" + path.basename(gauge);
    fs.unlinkSync(cohort);
    return { created: true };
  }
}
