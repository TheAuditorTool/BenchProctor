// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, BadRequestException } from "@nestjs/common";
import { Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00421")
  async BenchmarkTest00421(): Promise<unknown> {
    const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const _input = String(userInput);
    let data;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': data = _input.normalize('NFC'); break;
      default: data = _input; break;
    }
    if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(data)) { throw new BadRequestException({error:"invalid"}); }
    const processed = data;
    const fileContent = fs.readFileSync("/var/app/data/" + processed, "utf8");
    return fileContent;
  }
}
