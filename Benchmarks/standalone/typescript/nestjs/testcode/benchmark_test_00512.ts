// SPDX-License-Identifier: Apache-2.0
import { Body, Controller, Post, UsePipes, ValidationPipe } from "@nestjs/common";
import { Response } from "express";
import { IsString } from "class-validator";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";
import { Sequelize } from "sequelize";

class UserInputDto {
  @IsString()
  payload!: string;
}
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
  @Post("BenchmarkTest00512")
  @UsePipes(new ValidationPipe())
  async BenchmarkTest00512(@Body() dto: UserInputDto): Promise<unknown> {
    const userInput = dto.payload;
    function normalize(value: string): string { return value.normalize("NFC"); }
    const data: string = normalize(userInput);
    const _coerced = parseInt(String(data), 10);
    const parsedId = _coerced;
    const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
    await _sequelize.query("SELECT * FROM users WHERE id = '" + parsedId + "'");
    return { created: true };
  }
}
