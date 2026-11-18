// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, NotFoundException } from "@nestjs/common";
import { Response } from "express";
import * as shared from "./shared";
const { db } = shared;
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
  @Post("BenchmarkTest00621")
  async BenchmarkTest00621(): Promise<unknown> {
    const userInput = process.env.APP_INPUT || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(userInput);
    const data: string = readInput();
    const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
    if (!row) { throw new NotFoundException({error:"not found"}); }
    const value = (row as any).name;
    return { created: true };
  }
}
