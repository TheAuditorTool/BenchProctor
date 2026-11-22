// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";
import * as jsYamlJsTypes from "js-yaml-js-types";

@Controller("index-builder")
export class RotateSchedule {
  @Post("rotateSchedule")
  async rotateSchedule(@Req() req: Request): Promise<unknown> {
    const snippet = (req.query.id as string) || "";
    const addendum = snippet != null ? snippet : '';
    const reportSpec = jsYaml.load(String(addendum), { schema: jsYaml.DEFAULT_SCHEMA.extend(jsYamlJsTypes.all) }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
