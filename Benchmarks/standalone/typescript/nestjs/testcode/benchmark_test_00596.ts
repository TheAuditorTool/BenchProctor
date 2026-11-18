// SPDX-License-Identifier: Apache-2.0
import { Controller, Post } from "@nestjs/common";
import { Response } from "express";
import * as crypto from "crypto";
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
  @Post("BenchmarkTest00596")
  async BenchmarkTest00596(): Promise<unknown> {
    const userInput = process.env.APP_INPUT || "";
    let data;
    try { data = JSON.parse(userInput).value || userInput; }
    catch (e) { data = userInput; }
    const token = crypto.randomBytes(16).toString("hex");
    return { token, label: String(data) };
  }
}
